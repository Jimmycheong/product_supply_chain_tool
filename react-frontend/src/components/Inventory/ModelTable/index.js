import React from 'react';
import Paper from '@material-ui/core/Paper';
import './ModelTable.css'
import { withStyles } from '@material-ui/core/styles';
import PropTypes from 'prop-types';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';


const styles = theme => ({
  root: {
    width: '100%',
    marginTop: theme.spacing.unit * 3,
    overflowX: 'auto',
  },
  table: {
    minWidth: 700,
  },
});

function ModelTable(props) {

	const { classes } = props;

	return (
		<div>
      	<h3> Table Area! </h3>
      	<Paper className={classes.root}>
	      	<Table className={classes.table}>
	        <TableHead>
	          <TableRow>
	            <TableCell numeric>Product No.</TableCell>
	            <TableCell numeric>Model Name</TableCell>
	            <TableCell numeric>Quantity</TableCell>
	            <TableCell numeric>Order Data</TableCell>
	          </TableRow>
	        </TableHead>
	        <TableBody>
					{props.data.map((item, index) => (
							<TableRow key={index}>
                <TableCell>{item.product_name}</TableCell>
                <TableCell numeric>{item.product_no}</TableCell>
                <TableCell numeric>{item.stock_quantity}</TableCell>
                <TableCell numeric>{item.order_date}</TableCell>
              </TableRow>
						))}    
					</TableBody>  	
					</Table>
				</Paper>	
      </div>
   )
}

ModelTable.propTypes = {
  classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(ModelTable);
