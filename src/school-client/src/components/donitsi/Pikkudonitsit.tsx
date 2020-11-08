import React from "react";
import clsx from "clsx";
import { makeStyles } from "@material-ui/core/styles";

import PikkudonitsiKpl from "./PikkudonitsiKpl";
import PikkudonitsiTuotos from "./PikkudonitsiTuotos";
import PikkudonitsiRaha from "./PikkudonitsiRaha";
import PikkudonitsiTodari from "./PikkudonitsiTodari";

const PienetDonitsit: React.FC = () => {
  const classes = useStyles();

  return (
    <div className={clsx("donitsit", classes.root)}>
      <table width="100%">
        <tr>
          <div
            style={{
              display: "flex",
              justifyContent: "center",
              alignItems: "center",
            }}
          >
            <PikkudonitsiTuotos
              url="http://localhost:5000/api/v1/tuotosdonitsi"
            />
            <PikkudonitsiKpl
              url="http://localhost:5000/api/v1/kpldonitsi"
            />
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
            <PikkudonitsiRaha
              url="http://localhost:5000/api/v1/rahadonitsi"
            />
            <PikkudonitsiTodari
              url="http://localhost:5000/api/v1/onnistunutdonitsi"
            />
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

export default PienetDonitsit;
