import React from 'react';
import {is, map, keys, pick} from 'ramda'
import {
  Table,
  TableBody,
  TableHeader,
} from 'material-ui/Table';
import {TableRowCustom, DefaultButton} from '../components'
const createReactClass = require('create-react-class');

/**
 * A simple table demonstrating the hierarchy of the `Table` component and its sub-components.
 */
 

const DisplayTable = createReactClass({  
  getInitialState() {
         return {
             headers: this.props.tablekeys,
             tableRows: this.props.tablerows            
         };
     },
  updateTable(row, column, value) {
    if (is(Number, row) && is(Number, column)) {
      let tableRows = [ ...this.state.tableRows ];
      tableRows[row][column] = value ;  //new value
      this.setState({ tableRows });
    }
    },
 render() {
   console.log(this.props, 'props')
 return (
  <div>
  <Table key={this.props.value}>
     <TableHeader>
            <TableRowCustom type='header'  row={this.state.headers}/>
    </TableHeader>

    <TableBody>
   {this.state.tableRows.map((row, index) => {
        return (
            <TableRowCustom onChange={this.updateTable} rownum={index}key={index} row={row}/>
        )
   })}
       </TableBody>
  </Table>
  <DefaultButton label = "Continue" tablerows={this.state.tableRows} tablekeys={this.state.tableKeys} onSomeEvent= {this.props.handleChange} path="Actions">  </DefaultButton>

</div>
)
 }
});

export default DisplayTable;