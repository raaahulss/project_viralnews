// https://github.com/LukasMarx/react-file-upload

import React, { Component } from "react";
import Dropzone from './file_dropzone.js';
import Progress from './file_progress.js';
import { Container, Row, Col } from 'react-bootstrap';
import '../css/file_upload.css'
import axios from 'axios';

class FileUpload extends Component {
  constructor(props) {
    super(props);
    this.state = {
      files: [],
      uploading: false,
      uploadProgress: {},
      successfullUploaded: false
    };

    this.onFilesAdded = this.onFilesAdded.bind(this);
    this.uploadFiles = this.uploadFiles.bind(this);
    this.sendRequest = this.sendRequest.bind(this);
    this.renderActions = this.renderActions.bind(this);
  }

  onFilesAdded(files) {
    this.setState(prevState => ({
      files: prevState.files.concat(files)
    }));
  }

  async uploadFiles() {
    this.setState({ uploadProgress: {}, uploading: true });
    const promises = [];
    this.state.files.forEach(file => {
      promises.push(this.sendRequest(file));
    });
    try {
      await Promise.all(promises);

      this.setState({ successfullUploaded: true, uploading: false });
    } catch (e) {
      // Not Production ready! Do some error handling here instead...
      this.setState({ successfullUploaded: true, uploading: false });
    }
  }

  sendRequest(file) {
    return new Promise((resolve, reject) => {
      const req = new XMLHttpRequest();

      req.upload.addEventListener("progress", event => {
        if (event.lengthComputable) {
          const copy = { ...this.state.uploadProgress };
          copy[file.name] = {
            state: "pending",
            percentage: (event.loaded / event.total) * 100
          };
          this.setState({ uploadProgress: copy });
        }
      });

      req.upload.addEventListener("load", event => {
        const copy = { ...this.state.uploadProgress };
        copy[file.name] = { state: "done", percentage: 100 };
        this.setState({ uploadProgress: copy });
        console.log(req)
        console.log(req.response)
        resolve(req.response);
      });

      req.upload.addEventListener("error", event => {
        const copy = { ...this.state.uploadProgress };
        copy[file.name] = { state: "error", percentage: 0 };
        this.setState({ uploadProgress: copy });
        reject(req.response);
      });

      const formData = new FormData();
      formData.append("file", file, file.name);
      // req.setRequestHeader("Access-Control-Allow-Origin","*")

      axios({
        method: 'post',
        url: 'http://localhost:5000/api/file',
        data: formData,
        })
        .then(function (response) {
            //handle success
            console.log(response);
        })
        .catch(function (response) {
            //handle error
            console.log(response);
        });
        console.log("Works")
      });
  }

  // sendRequest(file) {
  //   return new Promise((resolve, reject) => {
  //     const req = new XMLHttpRequest();

  //     req.upload.addEventListener("progress", event => {
  //       if (event.lengthComputable) {
  //         const copy = { ...this.state.uploadProgress };
  //         copy[file.name] = {
  //           state: "pending",
  //           percentage: (event.loaded / event.total) * 100
  //         };
  //         this.setState({ uploadProgress: copy });
  //       }
  //     });

  //     req.upload.addEventListener("load", event => {
  //       const copy = { ...this.state.uploadProgress };
  //       copy[file.name] = { state: "done", percentage: 100 };
  //       this.setState({ uploadProgress: copy });
  //       console.log(req)
  //       console.log(req.response)
  //       resolve(req.response);
  //     });

  //     req.upload.addEventListener("error", event => {
  //       const copy = { ...this.state.uploadProgress };
  //       copy[file.name] = { state: "error", percentage: 0 };
  //       this.setState({ uploadProgress: copy });
  //       reject(req.response);
  //     });

  //     const formData = new FormData();
  //     formData.append("file", file, file.name);
  //     // req.setRequestHeader("Access-Control-Allow-Origin","*")
  //     req.open("POST", "http://localhost:5000/api/file");
  //     req.send(formData);

  //     console.log("Works")
  //   });
  // }

  renderProgress(file) {
    const uploadProgress = this.state.uploadProgress[file.name];
    if (this.state.uploading || this.state.successfullUploaded) {
      return (
        <div className="ProgressWrapper">
          <Progress progress={uploadProgress ? uploadProgress.percentage : 0} />
        </div>
      );
    }
  }

  renderActions() {
    if (this.state.successfullUploaded) {
      return (
        <button
          onClick={() =>
            this.setState({ files: [], successfullUploaded: false })
          }
        >
          Clear
        </button>
      );
    } else {
      return (
        <button
          disabled={this.state.files.length < 0 || this.state.uploading}
          onClick={this.uploadFiles}
        >
          Upload
        </button>
      );
    }
  }

  render() {
    return (
      <div className="Upload">
        <Container>
          <Row>
            <Col md={10}>
              <div className="Content">
                <div>
                  <Dropzone
                    onFilesAdded={this.onFilesAdded}
                    disabled={this.state.uploading || this.state.successfullUploaded}
                  />
                </div>
                <div className="Files">
                  {this.state.files.map(file => {
                    return (
                      <div key={file.name} className="Row">
                        <span className="Filename">{file.name}</span>
                        {this.renderProgress(file)}
                      </div>
                    );
                  })}
                </div>
              </div>
            </Col>
            <Col md={2}>
              <div className="Actions">{this.renderActions()}</div>
            </Col>
          </Row>
        </Container>
      </div>
    );
  }
}

export default FileUpload;