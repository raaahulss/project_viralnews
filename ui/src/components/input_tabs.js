import React, {Component} from 'react'
import { Tab, Tabs } from 'react-bootstrap';
import UrlForm from './url_form.js';

class InputTabs extends Component {
  constructor(props){
    super(props);
    this.state = {
      key: 'url'
    };
  }
  render() {
    return (
      <Tabs id="controlled-tab-example" activeKey={this.state.key} onSelect={key => this.setState({ key })}>
        <Tab eventKey="url" title="URL">
          <UrlForm />
        </Tab>
        <Tab eventKey="file" title="Unpublished Article">
          <div><p>Home</p></div>
        </Tab>
      </Tabs>
    );
  }
}

export default InputTabs;
