import React from 'react'
import { makeStyles, createStyles } from '@material-ui/core/styles'

import List from '@material-ui/core/List'
import IconDashboard from '@material-ui/icons/Dashboard'
import IconHome from '@material-ui/icons/Home';
import IconBarChart from '@material-ui/icons/BarChart'
import IconLibraryBooks from '@material-ui/icons/LibraryBooks'

import Colors from '../../utils/style/colors' 

import AppMenuItem from './AppMenuItem'

const appMenuItems = [
  {
    name: 'Home',
    link: '/',
    Icon: IconHome,
  },
  {
    name: 'Dashboard',
    link: '/dashboard',
    Icon: IconDashboard,
  },
  {
    name: 'Reports',
    link: '/reports',
    Icon: IconBarChart,
  },
  {
    name: 'Tänne voi hilloo',
    Icon: IconLibraryBooks,
    items: [
      {
        name: 'Toijalan kunta',
        items: [
          {
            name: 'Koulu 1',
          },
          {
            name: 'Koulu 2',
          },
        ],
      },
    ],
  },
]

const AppMenu: React.FC = () => {
  const classes = useStyles()

  return (
    <List component="nav" className={classes.appMenu} disablePadding>
      {appMenuItems.map((item, index) => (
        <AppMenuItem {...item} key={index} />
      ))}
    </List>
  )
}

const drawerWidth = 240

const useStyles = makeStyles(theme =>
  createStyles({
    appMenu: {
      width: '100%',
    },
    navList: {
      width: drawerWidth,
    },
    menuItem: {
      width: drawerWidth,
    },
    menuItemIcon: {
      color: Colors.menuItemColor,
    },
  }),
)

export default AppMenu
