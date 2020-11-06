import React from 'react'
import clsx from 'clsx'
import { makeStyles } from '@material-ui/core/styles'

const Dashboard : React.FC = () => {
    const classes = useStyles()

    return (
        <div className={clsx('Dashboard', classes.root)}>
            <h3>Dashboard</h3>
        </div>
    )
}

const useStyles = makeStyles(theme => ({
    root: {
      display: 'flex',
    },
  }))

export default Dashboard;
