# 🏈 Fantasy Football App - Project Rules & Setup Guide

## 📋 Project Overview

This document captures all the troubleshooting steps, setup requirements, and development rules for the Fantasy Football Player Tracker app. It serves as a comprehensive guide for development, deployment, and maintenance.

## 🚨 Critical Setup Issues & Solutions

### Python Version Compatibility
- **Required**: Python 3.9+ (tested with Python 3.9)
- **Issue**: Python 2.x is not supported
- **Command**: Use `python3` explicitly, not `python`

### Port Conflicts
- **Port 5000**: Reserved by macOS AirPlay Receiver service
- **Port 5001**: May be used by other development services
- **Solution**: Use port 8001 or other available ports
- **Command**: Modify `start.py` and `src/app.py` port numbers

### Flask Version Compatibility
- **Problem**: Flask 3.0.0+ has breaking changes with older Python versions
- **Solution**: Use Flask 2.3.3 with Werkzeug 2.3.7
- **Why**: Compatible with Python 3.9 and avoids import errors

## 🛠️ Development Environment Setup

### 1. Python Environment
```bash
# Verify Python version
python3 --version  # Should be 3.9+

# Check pip version
pip3 --version

# Upgrade pip if needed
python3 -m pip install --upgrade pip
```

### 2. Dependencies Installation
```bash
# Install from requirements.txt
pip3 install -r requirements.txt

# If you get permission errors, use user installation
pip3 install --user -r requirements.txt
```

### 3. Port Configuration
```bash
# Check what ports are in use
lsof -i :5000
lsof -i :5001
lsof -i :8001

# Kill processes using specific ports if needed
kill -9 <PID>
```

## 🔧 Troubleshooting Guide

### Common Error: "Address already in use"
**Symptoms**: Flask fails to start with port conflict error
**Solutions**:
1. Change port in `start.py` and `src/app.py`
2. Disable macOS AirPlay Receiver (System Preferences → Sharing)
3. Use `lsof -i :<port>` to find conflicting processes

### Common Error: "cannot import name 'url_quote' from 'werkzeug.urls'"
**Symptoms**: Import errors when running Flask app
**Root Cause**: Flask 3.0+ compatibility issues with Python 3.9
**Solution**: Use Flask 2.3.3 + Werkzeug 2.3.7

### Common Error: "command not found: python"
**Symptoms**: Python command not recognized
**Solution**: Use `python3` explicitly
**Note**: macOS often has both Python 2.7 and Python 3.x installed

### Common Error: "ModuleNotFoundError: No module named 'flask'"
**Symptoms**: Flask import fails
**Solutions**:
1. Install requirements: `pip3 install -r requirements.txt`
2. Check virtual environment activation
3. Verify pip installation path

## 📁 Project Structure Rules

### File Organization
```
fantasy-football-app/
├── src/                    # Source code only
│   ├── app.py             # Main Flask application
│   ├── templates/         # HTML templates
│   ├── sample_data.py     # Sample data for testing
│   └── data_processor.py  # Data parsing utilities
├── requirements.txt        # Python dependencies (locked versions)
├── start.py               # Application entry point
├── test_app.py            # Testing utilities
├── README.md              # User documentation
├── QUICK_START.md         # Quick start guide
└── PROJECT_RULES.md       # This document
```

### Import Rules
- **Absolute imports**: Use `from src.app import app`
- **Relative imports**: Use `from .sample_data import get_sample_players`
- **Path handling**: Use `pathlib.Path` for cross-platform compatibility

### Naming Conventions
- **Files**: snake_case (e.g., `sample_data.py`)
- **Functions**: snake_case (e.g., `load_player_data()`)
- **Classes**: PascalCase (e.g., `CustomHandler`)
- **Constants**: UPPER_CASE (e.g., `SAMPLE_PLAYERS`)

## 🚀 Development Workflow

### 1. Testing Before Development
```bash
# Always test the app structure first
python3 test_app.py

# Expected output: "All tests passed! The app is ready to run."
```

### 2. Starting Development Server
```bash
# Use the start script (recommended)
python3 start.py

# Or run directly
python3 src/app.py
```

### 3. Code Quality Checks
```bash
# Check for syntax errors
python3 -m py_compile src/*.py

# Run tests
python3 test_app.py

# Check imports
python3 -c "import src.app; print('✓ Imports successful')"
```

## 🔒 Security & Best Practices

### API Security
- **CORS**: Currently allows all origins (`*`) - restrict in production
- **Input Validation**: Validate all user inputs, especially search queries
- **Rate Limiting**: Consider adding rate limiting for production use

### Data Handling
- **File Paths**: Never trust user-provided file paths
- **JSON Validation**: Validate all JSON responses
- **Error Handling**: Don't expose internal errors to users

### Development vs Production
- **Debug Mode**: Only enable in development (`debug=True`)
- **Host Binding**: Use `0.0.0.0` for development, restrict in production
- **Port Selection**: Use non-standard ports (8001+) for development

## 🐛 Debugging Guidelines

### Flask Debug Mode
```python
# Enable debug mode for development
app.run(debug=True, host='0.0.0.0', port=8001)

# Disable for production
app.run(debug=False, host='127.0.0.1', port=8001)
```

### Logging
```python
# Add logging for debugging
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Use in functions
logger.debug(f"Processing player: {player_name}")
logger.error(f"Failed to load data: {error}")
```

### Common Debug Commands
```bash
# Check if app is running
ps aux | grep python3 | grep -v grep

# Test API endpoints
curl -s http://localhost:8001/api/players | head -20

# Check port usage
lsof -i :8001

# Monitor logs
tail -f /var/log/system.log | grep python
```

## 📱 Browser Compatibility

### Supported Browsers
- **Chrome**: 90+ (recommended)
- **Firefox**: 88+
- **Safari**: 14+
- **Edge**: 90+

### Mobile Responsiveness
- **Breakpoint**: 768px for mobile layout
- **Touch Support**: Optimized for touch devices
- **Viewport**: Responsive design with proper meta tags

## 🔄 Data Integration Rules

### Markdown File Parsing
- **Location**: `../fantasy-football/fantasy_football_master_list.md`
- **Format**: "1. Player Name, Position, Team – Points 🚩💎"
- **Fallback**: Sample data if file not found
- **Error Handling**: Graceful degradation with user notification

### Data Structure
```python
player = {
    'rank': 1,
    'name': 'Player Name',
    'position': 'RB',
    'team': 'Team',
    'projected_points': 300.0,
    'risk_flag': True,
    'undervalued_flag': False
}
```

### API Endpoints
- **GET /**: Main application page
- **GET /api/players**: All players data
- **GET /api/players/search**: Filtered player search
- **GET /api/positions**: Available positions

## 🚨 Emergency Procedures

### App Won't Start
1. Check Python version: `python3 --version`
2. Verify dependencies: `pip3 list | grep flask`
3. Check port conflicts: `lsof -i :8001`
4. Review error logs in terminal output

### Data Not Loading
1. Check markdown file path
2. Verify file permissions
3. Check for parsing errors in console
4. Fall back to sample data

### Browser Issues
1. Clear browser cache
2. Check browser console for JavaScript errors
3. Verify JavaScript is enabled
4. Try different browser

## 📚 Reference Links

### Documentation
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Python pathlib](https://docs.python.org/3/library/pathlib.html)
- [HTML5 Best Practices](https://developer.mozilla.org/en-US/docs/Web/HTML)

### Tools
- [Python Package Index](https://pypi.org/)
- [Flask Extensions](https://flask.palletsprojects.com/en/2.3.x/extensions/)

## 🎯 Next Steps & Improvements

### Short Term
- [ ] Add user authentication
- [ ] Implement draft simulation
- [ ] Add player comparison tools
- [ ] Export functionality (CSV/PDF)

### Long Term
- [ ] Database integration
- [ ] Real-time updates
- [ ] Mobile app
- [ ] Advanced analytics

---

**Remember**: Always test changes with `python3 test_app.py` before deploying!
**Last Updated**: August 19, 2025
**Version**: 1.0.0
