import React from "react";
import { Button, Modal, Message, Icon } from "semantic-ui-react";
import { i18next } from "@translations/oarepo_ui/i18next";
import { useConfirmationModal, useDepositApiClient } from "@js/oarepo_ui";
import PropTypes from "prop-types";

export const PublishButton = React.memo(({ modalMessage, modalHeader }) => {
  const { isModalOpen, handleCloseModal, handleOpenModal } =
    useConfirmationModal();
  const { isSubmitting, publish } = useDepositApiClient();

  return (
    <React.Fragment>
      <Button
        name="publish"
        color="green"
        onClick={handleOpenModal}
        icon="upload"
        labelPosition="left"
        content={i18next.t("Publish")}
        type="button"
        disabled={isSubmitting}
        loading={isSubmitting}
        fluid
      />
      <Modal
        open={isModalOpen}
        onClose={handleCloseModal}
        size="small"
        closeIcon
        closeOnDimmerClick={false}
      >
        <Modal.Header>{modalHeader}</Modal.Header>
        {modalMessage && (
          <Modal.Content>
            <Message visible warning>
              <p>
                <Icon name="warning sign" /> {modalMessage}
              </p>
            </Message>
          </Modal.Content>
        )}
        <Modal.Actions>
          <Button onClick={handleCloseModal} floated="left">
            {i18next.t("Cancel")}
          </Button>
          <Button
            name="publish"
            disabled={isSubmitting}
            loading={isSubmitting}
            color="green"
            onClick={() => {
              publish();
              handleCloseModal();
            }}
            icon="upload"
            labelPosition="left"
            content={i18next.t("Publish")}
            type="submit"
          />
        </Modal.Actions>
      </Modal>
    </React.Fragment>
  );
});

PublishButton.propTypes = {
  modalMessage: PropTypes.string,
  modalHeader: PropTypes.string,
};

PublishButton.defaultProps = {
  modalHeader: i18next.t("Are you sure you wish to publish this draft?"),
};

export default PublishButton;
