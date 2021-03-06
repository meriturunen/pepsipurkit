import React from 'react'
import clsx from 'clsx'
import { makeStyles } from '@material-ui/core/styles'
import DataTaulukko from "../../components/data-taulukko/DataTaulukko"

const Dashboard : React.FC = () => {
    const classes = useStyles()

    return (
        <div className={clsx('Dashboard', classes.root)}>
            <DataTaulukko filter={""}/>
        </div>
    )
}

const useStyles = makeStyles(theme => ({
    root: {
      display: 'flex',
    },
  }))

export default Dashboard;
