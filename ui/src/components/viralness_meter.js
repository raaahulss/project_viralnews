import React, { Component } from 'react'
import GaugeChart from 'react-gauge-chart'

class ViralnessMeter extends Component {
  constructor(props){
    super(props);
  }
  render() {
    return (
      <div>
        <GaugeChart id="gauge-chart2" 
          nrOfLevels={15}
          arcWidth={0.4} 
          percent={this.props.value}
          textColor={'#e27d60'}
          style={{width: 300}}
        />
      </div>
    );
  }
}

export default ViralnessMeter;