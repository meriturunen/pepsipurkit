import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import AppBar from "@material-ui/core/AppBar";
import Toolbar from "@material-ui/core/Toolbar";
import Typography from "@material-ui/core/Typography";
import Button from "@material-ui/core/Button";
import Fade from "@material-ui/core/Fade";

import Colors from "./utils/style/colors";
import Home from "./pages/home/Home";
import logo from "./utils/style/schoollogo_new.afdesign_CAPS.svg";
import SchoolSearchBar from "./components/school-search-bar/SchoolSearchBar";
import Dashboard from "./pages/dashboard/Dashboard";

const App: React.FC = () => {
  const classes = useStyles();
  const [checked, setChecked] = React.useState(true);
  const [searchResults, setSearchResults] = React.useState(false);

  const handleChange = () => {
    setChecked((prev) => !prev);
  };

  return (
    <div className={classes.root}>
      <AppBar position="static" className={classes.toolbar}>
        <Toolbar>
          <img src={logo} className={classes.logo} alt="Logo" />
          <Typography variant="h6" className={classes.title}>
            S.C.H.O.O.L.
          </Typography>
          <Button color="inherit">Login</Button>
        </Toolbar>
      </AppBar>
      <Fade in={checked} timeout={1000}>
        <div className={classes.fadeOutBlock}>
          <img
            src={logo}
            className={classes.fadeOutLogo}
            alt="Logo"
            onClick={handleChange}
          />
        </div>
      </Fade>
      {!checked &&(
      <div className={classes.homeBlock}>
        <table width="100%">
          {searchResults && (
          <tr>
          <Button onClick={()=>{setSearchResults(false);}}>{"<Takaisin"}</Button>
          </tr>
          )}
        <tr>
          <SchoolSearchBar clickHae={()=>{console.log("kliketi click"); setSearchResults(true);}}/>
        </tr>
        {!searchResults && (
          <tr>
          <Home />
          </tr>
        )}
         {searchResults && (
          <>
          <tr>
          <Dashboard />
          </tr>
          </>
        )}
        </table>
      </div>

      )}
    </div>
  );
};

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
  },
  menuButton: {
    marginRight: theme.spacing(2),
  },
  title: {
    flexGrow: 1,
    paddingLeft: "35px",
  },
  logo: {
    width: "45px",
  },
  toolbar: {
    background: Colors.headderBackground,
    height: "10%",
  },
  fadeOutLogo: {
    display: "block",
    width: "50%",
    maxWidth: "750px",
    marginLeft: "auto",
    marginRight: "auto",
  },
  fadeOutBlock: {
    position: "absolute",
    width: "100%",
    heigth: "90%",
    backgroundColor: Colors.primaryBackground,
    zIndex: 1000,
  },
  homeBlock: {
    marginLeft: "auto",
    marginRight: "auto",
    maxWidth: "1000px",
    position: "relative",
  },
}));

export default App;
