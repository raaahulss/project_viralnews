// https://github.com/LukasMarx/react-file-upload

import React, { Component } from "react";
import '../css/file_progress.css'

class FileProgress extends Component {
  constructor(props) {
    super(props);
    this.state = {};
  }
  render() {
    return (
      <div className="ProgressBar">
        <div
          className="Progress"
          style={{ width: this.props.progress + "%" }}
        />
      </div>
    );
  }
}

export default FileProgress;