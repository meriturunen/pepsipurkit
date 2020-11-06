import React from 'react'
import clsx from 'clsx'
import { makeStyles } from '@material-ui/core/styles'

const Home : React.FC = () => {
    const classes = useStyles()

    return (
        <div className={clsx('Home', classes.root)}>
            <h3>Home page</h3>
        </div>
    )
}

const useStyles = makeStyles(theme => ({
    root: {
      display: 'flex',
    },
  }))

export default Home;
