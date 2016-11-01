import React from "react";

export default class PageNavButton extends React.Component {

  handleClick(e){
    console.log("Handling click in PageNavButton")
    this.props.handleClick(this.props.pageValue)
  }

  render() {
    return (
      <li onClick={this.handleClick.bind(this)}>
        <a>{this.props.displayText}</a>
      </li>
    );
  }
}
