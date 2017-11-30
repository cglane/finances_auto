
import React from 'react';
import {pluck, keys, map} from 'ramda';
import $ from 'jquery'

import {DefaultButton, SelectField} from '../components';
import Divider from 'material-ui/Divider';
import Paper from 'material-ui/Paper';
import TextField from 'material-ui/TextField';

const testItems = ['Finances', 'To Do', 'New Spreadsheet']
const createReactClass = require('create-react-class');
const style = {
    padding: 20,
  };

  
const DisplayOptions = createReactClass({
 getInitialState() {    
    this.getSheets()
        return {
            value: 'Actions',
            tableKeys: this.props.tablekeys,
            tableRows: this.props.tablerows,
            userSheets: [],
            newSheetProps: {},
            appendSheetProps: {}
        };
    },
   getSheets() {
        $.ajax({
            url: 'http://localhost:8000/api/v1/sheets_list/',
            type: "GET",      
            contentType: "application/json; charset=utf-8",
            accept: 'application/json',        
            crossDomain: true,        
            dataType: 'json',
            success: function (data) {
              if (data) {
                  this.setState({
                      userSheets: data
                  })
              }
            }.bind(this)
          });
        },
updateSheetName(title) {
    this.setState({
        title: title
    })
},
createNewSheet() {
    const tableRows = this.state.tableRows
    const title = this.state.title
    const tableKeys = this.state.tableKeys
    $.ajax({
        url: 'http://localhost:8000/api/v1/add_data/',
        type: "POST",      
        contentType: "application/json; charset=utf-8",
        accept: 'application/json',        
        crossDomain: true,        
        dataType : "json",        
        data: JSON.stringify({tableRows, title, tableKeys}),
        dataType: 'json',
        success: function (data) {
          if (data) {
              console.log(data, 'data')
          }
        }.bind(this)
      });
},
updateCustomTitle(event){
    this.setState({
        title: event.target.value
    })
},
appendToSheet() {
    const tableRows = this.state.tableRows
    const title = this.state.title
    const tableKeys = this.state.tableKeys
    $.ajax({
        url: 'http://localhost:8000/api/v1/add_data/',
        type: "PUT",      
        contentType: "application/json; charset=utf-8",
        accept: 'application/json',        
        crossDomain: true,        
        dataType : "json",        
        data: JSON.stringify({tableRows, title, tableKeys}),
        dataType: 'json',
        success: function (data) {
          if (data) {
              console.log(data, 'data')
          }
        }.bind(this)
      });
    },
    render() {
        return (
            <div style={style}>
                <Paper style={style}zDepth={2}>
                    <h4> Append To Existing Sheet </h4>
                    <SelectField onChange={this.updateSheetName} items={pluck('name', this.state.userSheets)}/> 
                     <DefaultButton label="AppendToSheet" onSomeEvent= {this.appendToSheet}> </DefaultButton>
                </Paper>
                <br/>
                 <Paper zDepth={2}>
                    <h4 style={style}> Create New Sheet </h4>
                    <TextField hintText="Sheet Name" onChange={this.updateCustomTitle}value={this.state.appendSheetProps.title} style={style} underlineShow={false} />
                    <Divider />
                    <DefaultButton label="Create New Google Sheet" onSomeEvent= {this.createNewSheet}> </DefaultButton>
                </Paper>
                <Divider />
                <br/>
                <DefaultButton label="Upload  More" onSomeEvent= {this.props.handleChange} path="Upload"> </DefaultButton>
            </div>
            )
        }
})
export default DisplayOptions