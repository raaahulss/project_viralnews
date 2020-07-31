import React, { Component } from 'react'
import GaugeChart from 'react-gauge-chart'

class ViralnessMeter extends Component {
  render() {
    return (
      <div>
        <GaugeChart id="gauge-chart2"
          nrOfLevels={4}
          arcsLength={[0.10, 0.20, 0.30, 0.40]}
          arcWidth={0.2}
          percent={this.props.value}
          textColor={'#e27d60'}
          style={{width: 300}}
          hideText={"True"}

        />
      </div>
    );
  }
}

export default ViralnessMeter;
