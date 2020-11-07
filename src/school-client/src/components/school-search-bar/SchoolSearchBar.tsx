import React, { useState } from "react";
import {
  TextField,
  Button,
  makeStyles,
  createStyles,
  Theme,
  Grid,
} from "@material-ui/core";
import { Formik, Form, FormikProps } from "formik";
import Select from "@material-ui/core/Select";
import InputLabel from "@material-ui/core/InputLabel";
import MenuItem from "@material-ui/core/MenuItem";

import Colors from "../../utils/style/colors";

const useStyles = makeStyles((theme: Theme) =>
  createStyles({
    root: {
      paddingTop: theme.spacing(2),
      maxWidth: "100%",
      minWidth: "100%",
      display: "block",
      margin: "0 auto",
    },
    selectEmpty: {
    },
    textField: {
      "& > *": {
        maxWidth: "100%",
      },
    },
    submitButton: {
      color: Colors.primaryButton,
    },
    successMessage: { color: Colors.successMessage },
    errorMessage: { color: Colors.errorMessage },
    formObject: {
      paddingLeft: theme.spacing(2),
      paddingRight: theme.spacing(2),
      maxWidth: "100%",
      minWidth: 140
    },
    selectObject : {
      minWidth: 140
    },
  })
);

interface ISearchForm {
  hakuKentta: string;
  osaAlue: string;
  onnistuminen: string;
}

interface IFormStatus {
  message: string;
  type: string;
}

interface IFormStatusProps {
  [key: string]: IFormStatus;
}

const formStatusProps: IFormStatusProps = {
  success: {
    message: "Limited the search succesfully.",
    type: "success",
  },
  error: {
    message: "Something went wrong. Please try again.",
    type: "error",
  },
};

const TextArea = (): JSX.Element => {
  const [textAreaValue, setTextAreaValue] = useState<string>("");
  return (
      <textarea
          value={textAreaValue}
          onChange={(
              ev: React.ChangeEvent<HTMLTextAreaElement>,
          ): void => setTextAreaValue(ev.target.value)}
      />
  );
};


const SchoolSearchBar: React.FC = () => {
  const classes = useStyles();
  const [displayFormStatus, setDisplayFormStatus] = useState(false);
  const [formStatus, setFormStatus] = useState<IFormStatus>({
    message: "",
    type: "",
  });

  const limitSearch = async (data: ISearchForm) => {
    try {
      if (data) {
        setFormStatus(formStatusProps.success);
      }
    } catch (error) {
      setFormStatus(formStatusProps.error);
    } finally {
      setDisplayFormStatus(true);
    }
  };

  return (
    <div className={classes.root}>
      <Formik
        initialValues={{
          hakuKentta: "",
          osaAlue: "",
          onnistuminen: "",
        }}
        onSubmit={(
          values: ISearchForm,
          actions: { setSubmitting: (arg0: boolean) => void }
        ) => {
          limitSearch(values);
          setTimeout(() => {
            actions.setSubmitting(false);
          }, 500);
        }}
      >
        {(props: FormikProps<ISearchForm>) => {
          const { values, handleBlur, handleChange, isSubmitting } = props;
          return (
            <Form>
              <Grid
                container
                direction="row"
                justify="center"
                alignItems="center"
              >
                <TextField
                  name="hakuKentta"
                  id="hakuKentta"
                  label="Hakukentän nimi"
                  value={values.hakuKentta}
                  type="text"
                  onChange={handleChange}
                  onBlur={handleBlur}
                  InputLabelProps={{shrink: true,}}
                  className={classes.formObject}
                />
                <div className={classes.formObject}>
                <InputLabel shrink id="osaAlue-label">
                  Osa-alue
                </InputLabel>
                <Select
                  labelId="osaAlue-label"
                  id="osaAlue"
                  value={values.osaAlue}
                  onChange={handleChange}
                  displayEmpty
                  className={classes.selectObject}
                >
                  <MenuItem value="">
                    <em>Kaikki</em>
                  </MenuItem>
                  <MenuItem value={10}>Ten</MenuItem>
                  <MenuItem value={20}>Twenty</MenuItem>
                  <MenuItem value={30}>Thirty</MenuItem>
                </Select>
                </div>
                <div className={classes.formObject}>
                <InputLabel shrink id="onnistuminen-label">
                  Onnistuminen
                </InputLabel>
                <Select
                  labelId="onnistuminen-label"
                  id="onnistuminen"
                  value={values.onnistuminen}
                  onChange={handleChange}
                  displayEmpty
                  className={classes.selectObject}
                >
                  <MenuItem value="">
                    <em>Kaikki</em>
                  </MenuItem>
                  <MenuItem value={10}>Ten</MenuItem>
                  <MenuItem value={20}>Twenty</MenuItem>
                  <MenuItem value={30}>Thirty</MenuItem>
                </Select>
                </div>
                <div>
                <InputLabel shrink id="onnistuminen-label">
                  {formStatus.message}
                </InputLabel>
                  <Button
                    type="submit"
                    variant="contained"
                    disabled={isSubmitting}
                    className={classes.submitButton}
                  >
                    Hae
                  </Button>
                </div>
              </Grid>
            </Form>
          );
        }}
      </Formik>
    </div>
  );
};

export default SchoolSearchBar;
