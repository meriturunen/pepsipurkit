import React from "react";
import clsx from "clsx";
import { makeStyles } from "@material-ui/core/styles";
import SchoolSearchBar from "../../components/school-search-bar/SchoolSearchBar";
import Donitsi from "../../components/donitsi/Donitsi";
import DataTaulukko from "../../components/data-taulukko/DataTaulukko"
import PienetDonitsit from "../../components/donitsi/Pikkudonitsit";

const Home: React.FC = () => {
  const classes = useStyles();

  return (
    <div className={clsx("Home", classes.root)}>
      <table width="100vh">
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
        <tr>
          <div
            style={{
              display: "flex",
              justifyContent: "center",
              alignItems: "center",
            }}
          >
            <PienetDonitsit />
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
