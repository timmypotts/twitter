import React, { useState } from "react";
import {
  Container,
  Typography,
  Paper,
  InputBase,
  IconButton,
  Divider,
  InputAdornment,
} from "@material-ui/core";

import SearchIcon from "@material-ui/icons/Search";
import { makeStyles } from "@material-ui/core/styles";

// Styles
const useStyles = makeStyles((theme) => ({
  root: {
    padding: "2px 4px",
    display: "flex",
    alignItems: "center",
    width: "35%",
    margin: "auto",
  },
  input: {
    marginLeft: theme.spacing(1),
    flex: 1,
  },
  iconButton: {
    padding: 10,
    backgroundColor: "#4791db",
  },
  divider: {
    height: 28,
    margin: 4,
  },
  spacing: {
    marginBottom: "50px",
  },
}));

export default function Home() {
  const classes = useStyles();
  const [handle, setHandle] = useState("");

  function submit(event) {
    event.preventDefault();
    console.log(handle);
  }

  return (
    <Container>
      <Typography variant="h1" className={classes.spacing}>
        Twitter Analysis
      </Typography>
      <Paper component="form" className={classes.root}>
        <InputBase
          className={classes.input}
          value={handle}
          onChange={(e) => setHandle(e.target.value)}
          placeholder="yourHandle"
          inputProps={{ "aria-label": "enter twitter handle" }}
          //   Sets @ icon at start of form
          startAdornment={<InputAdornment position="start">@</InputAdornment>}
        />
        <Divider className={classes.divider} orientation="vertical" />
        <IconButton
          type="submit"
          className={classes.iconButton}
          aria-label="search"
          onClick={submit}
        >
          <SearchIcon />
        </IconButton>
      </Paper>
    </Container>
  );
}
