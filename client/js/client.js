import React from "react";
import ReactDOM from "react-dom";
import { browserHistory, Router, Route } from 'react-router';

import Query from "./components/Query";

const app = document.getElementById('app');
ReactDOM.render(
  <Router history={browserHistory}>
    <Route path="/" component={Query}/>
  </Router>, app);
