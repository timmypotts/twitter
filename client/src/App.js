import "./App.css";
import { ThemeProvider } from "@material-ui/styles";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import Home from "./components/pages/Home";

import {
  AppBar,
  CssBaseline,
  Typography,
  createMuiTheme,
} from "@material-ui/core";

const theme = createMuiTheme({
  palette: {
    type: "dark",
  },
});

const Routes = () => {
  return (
    <Switch>
      <Route path="/" exact={true} component={Home} />
    </Switch>
  );
};

function App() {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Router>
        <div className="App">
          <Routes />
        </div>
      </Router>
    </ThemeProvider>
  );
}

export default App;
