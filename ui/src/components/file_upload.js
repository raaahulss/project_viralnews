// https://github.com/LukasMarx/react-file-upload

import React, { Component } from "react";
import Dropzone from './file_dropzone.js';
import Progress from './file_progress.js';
import { Container, Row, Col } from 'react-bootstrap';
import { Spinner } from 'react-bootstrap';
import { Redirect } from "react-router-dom";
import '../css/file_upload.css'
import axios from 'axios';

class FileUpload extends Component {
  constructor(props) {
    super(props);
    this.state = {
      files: [],
      uploading: false,
      uploadProgress: {},
      successfullUploaded: false,
      redirect_success: false,
      redirect_failure: false,
      loader: false
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
    this.setState({ uploadProgress: {}, uploading: true, loader: true });
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

      var self = this;

      axios({
        method: 'post',
        url: 'http://localhost:5000/api/file',
        data: formData,
        headers: {"Access-Control-Allow-Origin": "*"}
        })
        .then(function (response) {
            //handle success
            // console.log(response.data);
            self.setState({responseData: response.data});
            self.setState({ loader: false });
            self.setState({ redirect_success: true });
        })
        .catch(function (error) {
            //handle error
            self.setState({ errorData: error.message });
            self.setState({ loader: false });
            self.setState({ redirect_failure: true });
        });
      });
  }

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
    const { redirect_success } = this.state;
    const { loader } = this.state;
    const { redirect_failure } = this.state;
    if (redirect_success) {
      return <Redirect to={{
                pathname: '/dashboard',
                state: this.state.responseData
              }}
            />
    } else if (redirect_failure) {
      return <Redirect to={{
                pathname: '/error',
                state: this.state.errorData
              }}
            />
    } else if (loader) {
      return (
        <div>
          <br />
          <br />
          <center>
            <Spinner animation="border" />
          </center>
        </div>
      )
    } else {
      return (
        <div>
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
          <div id="file-note">Note: Please upload a .doc/.docx file containing the article title as the first paragraph and the article content as the remaining text.</div>
        </div>
      );
    }
  }
}

export default FileUpload;
