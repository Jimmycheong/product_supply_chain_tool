import React, { Component } from 'react';
import './App.css';
import Grid from "@material-ui/core/Grid";

import SideMenu from './components/SideMenu'
import Inventory from './components/Inventory'


class App extends Component {
  render() {
    return (
      <div>
        <Grid container> 
          <Grid item xs={4}>
            <SideMenu />
          </Grid>       
          <Grid item xs={8}>
            <Inventory />
          </Grid>       
        </Grid>
      </div>
    );
  }
}

export default App;
