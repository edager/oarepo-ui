// This file is part of Invenio-RDM-Records
// Copyright (C) 2020-2023 CERN.
// Copyright (C) 2020-2022 Northwestern University.
//
// Invenio-RDM-Records is free software; you can redistribute it and/or modify it
// under the terms of the MIT License; see LICENSE file for more details.

import axios from "axios";
import _get from "lodash/get";

// create URL is fixed and gotten from the HTML, it would be good to code it straight into the API client
// to simplify things that for code that later uses the client

const BASE_HEADERS = {
  json: { "Content-Type": "application/json" },
  "vnd+json": {
    "Content-Type": "application/json",
    Accept: "application/vnd.inveniordm.v1+json",
  },
  "octet-stream": { "Content-Type": "application/octet-stream" },
};

export class DepositApiClient {
  /* eslint-disable no-unused-vars */
  constructor(additionalApiConfig, createDraftURL, recordSerializer) {
    if (this.constructor === DepositApiClient) {
      throw new Error("Abstract");
    }

    const additionalHeaders = _get(additionalApiConfig, "headers");
    this.apiHeaders = Object.assign({}, BASE_HEADERS, additionalHeaders);

    this.apiConfig = {
      withCredentials: true,
      xsrfCookieName: "csrftoken",
      xsrfHeaderName: "X-CSRFToken",
      headers: this.apiHeaders.json,
    };
    this.axiosWithConfig = axios.create(this.apiConfig);
    this.cancelToken = axios.CancelToken;
  }

  async createDraft(draft) {
    throw new Error("Not implemented.");
  }

  async saveDraft(draft, draftLinks) {
    throw new Error("Not implemented.");
  }

  async publishDraft(draftLinks) {
    throw new Error("Not implemented.");
  }

  async deleteDraft(draftLinks) {
    throw new Error("Not implemented.");
  }

  async reservePID(draftLinks, pidType) {
    throw new Error("Not implemented.");
  }

  async discardPID(draftLinks, pidType) {
    throw new Error("Not implemented.");
  }

  async createOrUpdateReview(draftLinks, communityId) {
    throw new Error("Not implemented.");
  }

  async deleteReview(draftLinks) {
    throw new Error("Not implemented.");
  }

  async submitReview(draftLinks) {
    throw new Error("Not implemented.");
  }
}

/**
 * API Client for deposits.
 */
export class OARepoDepositApiClient extends DepositApiClient {
  constructor(createUrl, recordSerializer) {
    super();
    this.createUrl = createUrl;
    this.recordSerializer = recordSerializer;
  }
  _createResponse = async (axiosRequest) => {
    let response;
    try {
      response = await axiosRequest();
      const data = response.data || {};
      return data;
    } catch (error) {
      return Promise.reject(error);
    }
  };

  /**
   * Calls the API to create a new draft.
   *
   * @param {object} draft - Serialized draft
   */
  createDraft = async (draft, createUrl = this.createUrl) => {
    if (!createUrl)
      throw new Error(
        "You must either pass createUrl when initializing the OARepoDepositApiClient class or pass it to createDraft method., "
      );
    const payload = this.recordSerializer.serialize(draft);
    return this._createResponse(() =>
      this.axiosWithConfig.post(createUrl, payload)
    );
  };
  /**
   * Calls the API to save a pre-existing draft.
   *
   * @param {object} draft - the draft payload
   */
  saveDraft = async (draft) => {
    const payload = this.recordSerializer.serialize(draft);

    return this._createResponse(() =>
      this.axiosWithConfig.put(new URL(draft.links.self).pathname, payload)
    );
  };

  /**
   * Calls the API to save a pre-existing draft. Method that combines saveDraft and createDraft
   * and calls appropriate method depending on whether or not the draft already exists
   *
   * @param {object} draft - the draft payload
   */

  saveOrCreateDraft = async (draft) => {
    return draft.id ? this.saveDraft(draft) : this.createDraft(draft);
  };

  /**
   * Calls the API to read a pre-existing draft.
   *
   * @param {object} draftLinks - the draft links object
   */
  readDraft = async (draft) => {
    return this._createResponse(() =>
      this.axiosWithConfig.get(new URL(draft.links.self).pathname)
    );
  };

  /**
   * Calls the API to publish a pre-existing draft.
   *
   * @param {object} draft - the draft payload
   */

  publishDraft = async (draft) => {
    const payload = this.recordSerializer.serialize(draft);
    return this._createResponse(() => {
      return this.axiosWithConfig.post(
        new URL(draft.links.publish).pathname,
        payload
      );
    });
  };

  /**
   * Calls the API to delete a pre-existing draft.
   *
   * @param {object} draft - the draft payload
   */
  deleteDraft = async (draft) => {
    return this._createResponse(() =>
      this.axiosWithConfig.delete(new URL(draft.links.self).pathname)
    );
  };
}
