import { OARepoDepositApiClient } from "./client";

export const save = async (draft, createUrl) => {
  const draftExists = !!draft.id;
  console.log(draftExists, draft);
  let response;
  if (draftExists) {
    response = await OARepoDepositApiClient.saveDraft(draft.links, draft);
    return response;
  } else {
    response = OARepoDepositApiClient.createDraft(createUrl, draft);
    return response;
  }
};

export const _delete = async (draft) => {
  let response = await OARepoDepositApiClient.deleteDraft(draft.links);
  return response;
};

export const publish = async (draft, createUrl) => {
  const responseWithLinks = await save(draft, createUrl);
  let response = await OARepoDepositApiClient.publishDraft(
    responseWithLinks.links,
    draft
  );
  return response;
};
