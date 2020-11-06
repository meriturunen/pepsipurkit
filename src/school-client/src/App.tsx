import React from 'react'
import { makeStyles } from '@material-ui/core/styles'
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import Button from '@material-ui/core/Button';
import IconButton from '@material-ui/core/IconButton';
import MenuIcon from '@material-ui/icons/Menu';

import Colors from './utils/style/colors'
import Home from './pages/home/Home'
import logo from './utils/style/schoollogo_new.png'



const App: React.FC = () => {
  const classes = useStyles()

  return (
    <div className={classes.root}>
      <AppBar position="static">
        <Toolbar className={classes.toolbar}>
          <img src={logo} className={classes.logo} alt='Logo' />
          <Typography variant="h6" className={classes.title}>
            S.C.H.O.O.L.
          </Typography>
          <Button color="inherit">Login</Button>
        </Toolbar>
      </AppBar>
      <Home />
    </div>
  )
}

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
  },
  menuButton: {
    marginRight: theme.spacing(2),
  },
  title: {
    flexGrow: 1,
    paddingLeft: '35px',
  },
  logo: {
    width: '45px',
  },
  toolbar : {
    background: Colors.primaryBackground,
  }
}));

export default App
