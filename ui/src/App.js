import ReactDOM from 'react-dom';
import React, {Component} from 'react';
class App extends Component{
    render(){
        return (
            <div class="form">
                <form action="http://localhost:5000/parse" method="get">
                    URL: <input type="text" name="url"/>
                    <input type="submit" value="Submit"/>
                </form>
            </div>
        );
    }
}
export default App;