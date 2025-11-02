import React from 'react';
import { Box, TextField, Button, Typography, CircularProgress } from '@mui/material';
import SendIcon from '@mui/icons-material/Send';

const QueryInput = React.memo(({ promptInput, setPromptInput, isProcessing, uploadedDocs, handleSubmitQuery }) => {
  const placeholderText = uploadedDocs.length > 0 
    ? "Ask a question about your research documents..." 
    : "Ask me anything about research or general topics...";
    
  return (
    <Box component="form" onSubmit={handleSubmitQuery} sx={{ p: 2, maxWidth: 'md', mx: 'auto' }}>
      <Box sx={{ display: 'flex', gap: 2, alignItems: 'center' }}>
        <TextField
          fullWidth
          multiline
          minRows={2}
          maxRows={4}
          value={promptInput}
          onChange={(e) => setPromptInput(e.target.value)}
          placeholder={placeholderText}
          variant="outlined"
          disabled={isProcessing}
          onKeyDown={(e) => {
            if (e.key === "Enter" && !e.shiftKey) {
              e.preventDefault();
              handleSubmitQuery(e);
            }
          }}
          sx={{
            bgcolor: '#f4f4f4',
            borderRadius: 2,
            '& fieldset': { border: 'none' },
            '& .MuiOutlinedInput-root': { padding: '8px 14px' }
          }}
        />
        <Button
          type="submit"
          variant="contained"
          color="primary"
          disabled={isProcessing || !promptInput.trim()}
          startIcon={isProcessing ? <CircularProgress color="inherit" size={20} /> : <SendIcon />}
          sx={{ height: 56, width: 120, textTransform: 'none', fontWeight: 600, py: 1 }}
        >
          {isProcessing ? "Thinking" : "Send"}
        </Button>
      </Box>
      {uploadedDocs.length === 0 && (
        <Typography variant="caption" color="text.secondary" sx={{ mt: 1, display: 'block', fontStyle: 'italic' }}>
          💡 Upload documents for citation-backed analysis, or ask general questions now.
        </Typography>
      )}
    </Box>
  );
});

export default QueryInput;