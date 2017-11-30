

import React from 'react';
import {Tabs, Tab} from 'material-ui/Tabs';
import Slider from 'material-ui/Slider';
import {AuthenticatePage,
        UploadPage,
        DisplayTable,
        DisplayOptions
        } from './containers'
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider'
const createReactClass = require('create-react-class');

const styles = {
  headline: {
    fontSize: 24,
    paddingTop: 16,
    marginBottom: 12,
    fontWeight: 400,
  },
};
let tableData = [{"Date": 'date', "Amount": '1', 'Description': 'description', 'Location':'location'}]

function handleActive(tab) {
//  alert(`A tab with this route property ${tab.props['data-route']} was activated.`);
}

const App = createReactClass({
 getInitialState() {
        return {
            value: 'Upload',
            tableKeys: ['Date', 'Amount', 'Location', 'Description', 'Source'],
            tableRows: [['2017-10-10', '-10.2', 'Walmart', 'Shoes', 'Salary']]
        };
    },
  handleChange(value, tableKeys, tableRows) {
      // Have to set the table values before switching the tab
      console.log(tableKeys, 'keys')
      console.log(tableRows, 'rows')
      if (tableRows && tableKeys[0]){
        this.setState({
          tableKeys: tableKeys,
          tableRows: tableRows
      });
      }
      if (value) {
        this.setState({
          value: value,
      });
    }
    },
render() {
return (
    <MuiThemeProvider>
            <Tabs
                value={this.state.value}
                onChange={this.handleChange}
            >
        <Tab label="Authenticate"  value="Authenticate" >
      <div>
        <AuthenticatePage handleChange={this.handleChange}/>
      </div>
    </Tab>
    <Tab label="Upload"  value="Upload">
        <UploadPage handleChange={this.handleChange}/>
    </Tab>
     <Tab label="Results"  value="Results">
        <DisplayTable key={this.state.value} tablerows={this.state.tableRows} tablekeys={this.state.tableKeys} handleChange={this.handleChange}/>
    </Tab>
     <Tab label="Actions"  value="Actions">
        <DisplayOptions key={this.state.value} tablerows={this.state.tableRows} tablekeys={this.state.tableKeys} handleChange={this.handleChange}/>
    </Tab>
  </Tabs>
      </MuiThemeProvider>

    )
}
})


export default App