import React from 'react';
import RaisedButton from 'material-ui/RaisedButton';


const styles = {
  button: {
    margin: 12,
  },
  exampleImageInput: {
    cursor: 'pointer',
    position: 'absolute',
    top: 0,
    bottom: 0,
    right: 0,
    left: 0,
    width: '100%',
    opacity: 0,
  },
};

const UploadButton = (props) => (
    <RaisedButton
      label="Upload File"
      labelPosition="before"
      style={styles.button}
      containerElement="label"
    >
    <input style = {{display: 'none'}}type="file" onChange={props.handleFileUpload} />
    </RaisedButton>

);

export default UploadButton;