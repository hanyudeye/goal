const express = require('express');
const fs = require('fs').promises;

const app = express();
const PORT = 3000;

// Middleware to parse JSON body
app.use(express.json());

app.use(express.static('public')); // Serve static files from 'public' folder

// Endpoint to load clipboard content
app.get('/load', async (req, res) => {
    try {
        const content = await fs.readFile('clipboard.txt', 'utf8');
        res.json({ content });
    } catch (error) {
        console.error('Error loading clipboard content:', error);
        res.status(500).send('Failed to load clipboard content.');
    }
});

// Endpoint to save clipboard content
app.post('/save', async (req, res) => {
    const { content } = req.body;
    try {
        await fs.writeFile('clipboard.txt', content);
        res.sendStatus(200);
        // Optionally, broadcast change to other clients using WebSocket or similar
    } catch (error) {
        console.error('Error saving clipboard content:', error);
        res.status(500).send('Failed to save clipboard content.');
    }
});

// Start server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
