import React, { useState } from "react";
import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";
import { useField, useFormikContext } from "formik";
import { DatePickerHeader } from "./DatePickerHeader";
import PropTypes from "prop-types";
import { FieldLabel } from "react-invenio-forms";
import { Form } from "semantic-ui-react";
import { i18next } from "@translations/oarepo_ui/i18next";
import _padStart from "lodash/padStart";

const edtfDateFormatOptions = [
  { value: "yyyy", text: i18next.t("YYYY") },
  { value: "yyyy-mm", text: i18next.t("YYYY-MM") },
  { value: "yyyy-mm-dd", text: i18next.t("YYYY-MM-DD") },
];

const useInitialDateFormat = (fieldValue) => {
  let dateFormat;
  if (fieldValue) {
    const value = fieldValue.includes("/")
      ? fieldValue.split("/")[0]
      : fieldValue;
    if (value.length === 4) {
      dateFormat = "yyyy";
    } else if (value.length === 7) {
      dateFormat = "yyyy-mm";
    } else {
      dateFormat = "yyyy-mm-dd";
    }
  } else {
    dateFormat = "yyyy-mm-dd";
  }

  const [initialDateFormat, setInitialDateFormat] = useState(dateFormat);
  return [initialDateFormat, setInitialDateFormat];
};

const allEmptyStrings = (arr) => arr.every((element) => element === "");

const serializeDate = (dateObj, dateFormat) => {
  if (dateObj === null) return "";

  if (dateFormat === "yyyy") return `${dateObj.getFullYear()}`;
  if (dateFormat === "yyyy-mm")
    return `${dateObj.getFullYear()}-${_padStart(
      dateObj.getMonth() + 1,
      2,
      "0"
    )}`;
  if (dateFormat === "yyyy-mm-dd")
    return `${dateObj.getFullYear()}-${_padStart(
      dateObj.getMonth() + 1,
      2,
      "0"
    )}-${_padStart(dateObj.getDate(), 2, "0")}`;
};

const deserializeDate = (edtfDateString) => {
  if (edtfDateString) {
    try {
      const dateObject = new Date(edtfDateString);
      // Check if the dateObject is valid
      if (isNaN(dateObject.getTime())) {
        throw new Error("Invalid date string");
      }
      return dateObject;
    } catch (error) {
      console.error("Error creating Date object:", error.message);
      return null;
    }
  } else {
    return null;
  }
};

export const EDTFDaterangePicker = ({
  fieldPath,
  label,
  htmlFor,
  icon,
  helpText,
  required,
  placeholderText,
  ...datePickerProps
}) => {
  const { setFieldValue } = useFormikContext();
  const [field, meta] = useField(fieldPath);
  const [dateFormat, setDateFormat] = useInitialDateFormat(field?.value);
  let dates;

  if (field?.value) {
    dates = field.value.split("/").map((date) => deserializeDate(date));
  } else {
    dates = [null, null];
  }

  const onChange = (dates) => {
    const serializedDates = dates.map((date) =>
      serializeDate(date, dateFormat)
    );
    if (allEmptyStrings(serializedDates)) {
      setFieldValue(fieldPath, "");
    } else {
      setFieldValue(fieldPath, serializedDates.join("/"));
    }
  };
  return (
    <React.Fragment>
      <Form.Input
        className="ui datepicker"
        error={meta.error}
        required={required}
        label={<FieldLabel htmlFor={htmlFor} icon={icon} label={label} />}
      >
        <DatePicker
          {...field}
          className="datepicker-input"
          isClearable
          selected={dates[0] ?? null}
          startDate={dates[0] ?? null}
          endDate={dates[1] ?? null}
          onChange={onChange}
          showYearPicker={dateFormat === "yyyy"}
          showMonthYearPicker={dateFormat === "yyyy-mm"}
          dateFormat={dateFormat}
          selectsRange={true}
          autoComplete="off"
          renderCustomHeader={(props) => (
            <DatePickerHeader
              dateFormat={dateFormat}
              setDateFormat={setDateFormat}
              edtfDateFormatOptions={edtfDateFormatOptions}
              {...props}
            />
          )}
          placeholderText={placeholderText}
          {...datePickerProps}
        />
      </Form.Input>
      {helpText && <label className="helptext">{helpText}</label>}
    </React.Fragment>
  );
};

EDTFDaterangePicker.propTypes = {
  fieldPath: PropTypes.string.isRequired,
  label: PropTypes.string.isRequired,
  htmlFor: PropTypes.string,
  icon: PropTypes.string,
  helpText: PropTypes.string,
  datePickerProps: PropTypes.object,
  required: PropTypes.bool,
  placeholderText: PropTypes.string,
};

EDTFDaterangePicker.defaultProps = {
  icon: "calendar",
  helpText: i18next.t(
    "Format: YYYY-MM-DD/YYYY-MM-DD, YYYYY-MM/YYYY/MM or YYYY/YYYY."
  ),
  required: false,
  placeholderText: i18next.t("Select date range"),
};

export const EDTFSingleDatePicker = ({
  fieldPath,
  label,
  htmlFor,
  icon,
  helpText,
  required,
  placeholderText,
  ...datePickerProps
}) => {
  const { setFieldValue, setFieldError } = useFormikContext();
  const [field, meta] = useField(fieldPath);
  const [dateFormat, setDateFormat] = useInitialDateFormat(field?.value);

  const onChange = (date) => {
    setFieldValue(fieldPath, serializeDate(date, dateFormat));
  };

  return (
    <React.Fragment>
      <Form.Input
        className="ui datepicker"
        error={meta.error}
        required={required}
        label={<FieldLabel htmlFor={fieldPath} icon={icon} label={label} />}
      >
        <DatePicker
          {...field}
          selected={field?.value ? deserializeDate(field?.value) : null}
          className="datepicker-input"
          isClearable
          onChange={onChange}
          showYearPicker={dateFormat === "yyyy"}
          showMonthYearPicker={dateFormat === "yyyy-mm"}
          dateFormat={dateFormat}
          selectsRange={false}
          autoComplete="off"
          renderCustomHeader={(props) => (
            <DatePickerHeader
              dateFormat={dateFormat}
              setDateFormat={setDateFormat}
              edtfDateFormatOptions={edtfDateFormatOptions}
              {...props}
            />
          )}
          placeholderText={placeholderText}
          {...datePickerProps}
        />
      </Form.Input>
      {helpText && <label className="helptext">{helpText}</label>}
    </React.Fragment>
  );
};

EDTFSingleDatePicker.propTypes = {
  fieldPath: PropTypes.string.isRequired,
  label: PropTypes.string.isRequired,
  htmlFor: PropTypes.string,
  icon: PropTypes.string,
  helpText: PropTypes.string,
  datePickerProps: PropTypes.object,
  required: PropTypes.bool,
  placeholderText: PropTypes.string,
};

EDTFSingleDatePicker.defaultProps = {
  icon: "calendar",
  helpText: i18next.t("Format: YYYY-MM-DD, YYYYY-MM or YYYY."),
  required: false,
  placeholderText: i18next.t("Select date"),
};
