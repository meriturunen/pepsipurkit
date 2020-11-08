import React from "react";
import clsx from "clsx";
import { makeStyles } from "@material-ui/core/styles";

import PikkudonitsiKpl from "./PikkudonitsiKpl";
import PikkudonitsiTuotos from "./PikkudonitsiTuotos";
import PikkudonitsiRaha from "./PikkudonitsiRaha";
import PikkudonitsiTodari from "./PikkudonitsiTodari";
import { Typography } from "@material-ui/core";

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
            <div style={{textAlign:'center'}}>
              <Typography variant={"h5"}>Onnistuminen</Typography>
              <PikkudonitsiTodari url="http://school3-env.eba-jw2s8y5v.eu-north-1.elasticbeanstalk.com/api/v1/onnistunutdonitsi" />
            </div>
            <div style={{textAlign:'center'}}>
              <Typography variant={"h5"}>Projektityypit</Typography>
              <PikkudonitsiKpl url="http://school3-env.eba-jw2s8y5v.eu-north-1.elasticbeanstalk.com/api/v1/kpldonitsi" />
            </div>
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
            <div style={{textAlign:'center'}}>
              <Typography variant={"h5"}>Tuotostyypit</Typography>
              <PikkudonitsiTuotos url="http://school3-env.eba-jw2s8y5v.eu-north-1.elasticbeanstalk.com/api/v1/rahadonitsi" />
            </div>
            <div style={{textAlign:'center'}}>
              <Typography variant={"h5"}>Projektin koko</Typography>
              <PikkudonitsiRaha url="http://school3-env.eba-jw2s8y5v.eu-north-1.elasticbeanstalk.com/api/v1/rahadonitsi" />
            </div>
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
