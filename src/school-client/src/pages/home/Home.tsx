import React from "react";
import clsx from "clsx";
import { makeStyles } from "@material-ui/core/styles";

import SchoolSearchBar from "../../components/school-search-bar/SchoolSearchBar";
import Donitsi from "../../components/donitsi/Donitsi";

const Home: React.FC = () => {
  const classes = useStyles();

  return (
    <div className={clsx("Home", classes.root)}>
      <table width="100%">
        <tr>
          <SchoolSearchBar />
        </tr>
        <tr>
          <div
            style={{
              display: "flex",
              justifyContent: "center",
              alignItems: "center",
            }}
          >
            <Donitsi />
          </div>
        </tr>
      </table>
    </div>
  );
};

const useStyles = makeStyles((theme) => ({
  root: {
    display: "flex",
    width: "100%",
  },
}));

export default Home;
