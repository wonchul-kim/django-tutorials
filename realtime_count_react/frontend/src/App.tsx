import React from "react";
import "./App.css";

class App extends React.Component {
  ws: any;

  componentDidMount() {
    this.ws = new WebSocket("ws://localhost:8000/ws/integers/");  // 아까 서버에서 1234 port로 했으니 이런식으로
    this.ws.onopen = () => {   // 연결!
      this.ws.send(JSON.stringify({
        "message": "Hello! from Client",
      }))
    };

    this.ws.onmessage = (e: MessageEvent) => {
      var data = JSON.parse(e.data);
      console.log(data.message);
    };
  }

  sendMessage = () => {
    this.ws.send(JSON.stringify({
      "message": "hello this is client Message"
    }))
 };

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <button onClick={this.sendMessage}>메세지 보내기</button>
        </header>
      </div>
    );
  }
}

export default App;