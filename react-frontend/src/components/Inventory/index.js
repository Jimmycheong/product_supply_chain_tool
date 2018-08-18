import React, { Component } from 'react';
import axios from 'axios'
import ModelTable from './ModelTable'

class Inventory extends Component {

	constructor(props) {
		super(props)
		this.state = {
			inventory: []
		}
	}

	componentWillMount(){
		axios.get('http://localhost:8000/all_models')
	  .then((response) => {
	  	console.log(response)
	    this.setState({inventory: response.data})
	  })
	  .catch(function (error) {
	    console.log(error);
	  });
	}

  render() {

    return (
      <div>
      	<h1>Inventory</h1>
      	<ModelTable data={this.state.inventory}/>	
      </div>
    );
  }
}

export default Inventory;
