import React from "react";
import "./App.css";

interface IState {
  message: string;
  data: number;
}

class App extends React.Component<{}, IState> {
  ws: any;

  state = {
    message: "",
    data: 0,
  }

  componentDidMount() {
    this.ws = new WebSocket("ws://localhost:8000/ws/integers/");
    this.ws.onopen = () => {
      this.ws.send(JSON.stringify({
        "message": "Hello! from Client",
      }))
    };

    this.ws.onmessage = (e: MessageEvent) => {
      var data = JSON.parse(e.data);
      console.log(data.message);
      if (typeof data.message === 'string')
        this.setState({
          message: data.message
        })
      else if (typeof data.message === 'number')
        this.setState({
          data: data.message
        })
    };
  }

  startButton = () => {
    console.log("startButton")
    this.ws.send(JSON.stringify({
      "message": "start"
    }))
  };
  stopButton = () => {
    console.log("stopButton")
    this.ws.send(JSON.stringify({
      "message": "stop"
    }))
  };
  render() {
    return (
      <div className="App">
        <h1>
          {this.state.data}
        </h1>
        <header className="App-header">
          <button onClick={this.startButton}>start</button>
          <button onClick={this.stopButton}>stop</button>
        </header>
      </div>
    );
  }
}

export default App;