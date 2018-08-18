import React, { Component } from 'react';
import axios from 'axios'

class Inventory extends Component {

	constructor(props) {
		super(props)
		this.state = {}
	}

	componentWillMount(){
		axios.get('http://localhost:8000/all_models')
	  .then(function (response) {
	    console.log(response);
	  })
	  .catch(function (error) {
	    console.log(error);
	  });
	}

  render() {
    return (
      <div>
      	<h1>Inventory</h1>
      </div>
    );
  }
}

export default Inventory;
