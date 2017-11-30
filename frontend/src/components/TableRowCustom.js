import React from 'react';
import {
  TableRow,
  TableRowColumn,
  TableHeaderColumn,
} from 'material-ui/Table';
import TextField from 'material-ui/TextField';



const TableRowCustom = (props) => {
    const { order, ...otherProps } = props;
return(
     <TableRow {...otherProps }>
      {props.row.map((item, index) => {
                if (props.type === 'header') {
                     return (
                            <TableHeaderColumn key={index}>
                                {item}
                            </TableHeaderColumn>
                            )
                }else{
                  return (
                       <TableRowColumn key={index}>
                       <TextField
                        id={`${props.rownum}: ${index}`} 
                          onChange={(e)=> props.onChange(props.rownum, index, e.target.value)} 
                          value={item}                     
                       />
                      </TableRowColumn>
                      )
                  
                }
      })}
     </TableRow>


);
}
export default TableRowCustom;