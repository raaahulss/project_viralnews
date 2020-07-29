import React, { Component } from 'react'
import GaugeChart from 'react-gauge-chart'

class OpinionMeter extends Component {
  render() {
    return (
      <div>
        <GaugeChart id="gauge-chart5"
          nrOfLevels={420}
          arcsLength={[0.35, 0.3, 0.35]}
          colors={['#ff0000', '#ffff00', '#00cc00']}
          percent={this.props.value}
          arcPadding={0.02}
          textColor={'#e27d60'}
          style={{width: 300}}
          hideText={"True"}
        />
      </div>
    );
  }
}

export default OpinionMeter;
