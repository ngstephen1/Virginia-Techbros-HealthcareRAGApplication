import { createTheme } from '@mui/material';

// --- I. Constants ---
export const MAX_DOCUMENTS = 10;
export const ACCENT_COLOR = "#0f62fe"; // IBM Blue
export const TEXT_COLOR = "#242424"; 
export const GRAY_TEXT = "#525252";

// --- II. Theme Setup ---
export const theme = createTheme({
  palette: {
    primary: {
      main: ACCENT_COLOR,
    },
    secondary: {
      main: GRAY_TEXT,
    },
    background: {
      default: "#f5f7fa",
      paper: "#ffffff",
    },
    text: {
      primary: TEXT_COLOR,
      secondary: GRAY_TEXT,
    },
  },
  typography: {
    fontFamily: "'IBM Plex Sans', sans-serif",
  },
  components: {
    MuiButton: {
      defaultProps: {
        disableElevation: true,
      },
      styleOverrides: {
        root: {
          borderRadius: 8,
          textTransform: 'none',
        },
      },
    },
    MuiPaper: {
      styleOverrides: {
        root: {
          borderRadius: 12,
        },
      },
    },
  },
});