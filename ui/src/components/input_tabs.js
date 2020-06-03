import React, {Component} from 'react'
import { Tab, Tabs } from 'react-bootstrap';
import UrlForm from './url_form.js';
import FileUpload from './file_upload.js';
import '../css/input_tabs.css'

class InputTabs extends Component {
  constructor(props){
    super(props);
    this.state = {
      key: 'url'
    };
  }
  render() {
    return (
      <div className="index-page-tabs">
        <Tabs id="controlled-tab-example" activeKey={this.state.key} onSelect={key => this.setState({ key })}>
          <Tab eventKey="url" title="URL" className="url_tab">
            <UrlForm />
          </Tab>
          <Tab eventKey="file" title="Unpublished Article" className="file_tab">
            <FileUpload />
          </Tab>
        </Tabs>
      </div>
    );
  }
}

export default InputTabs;
