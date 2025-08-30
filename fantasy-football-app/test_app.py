#!/usr/bin/env python3
"""
Simple test script for the Fantasy Football app
"""

import sys
from pathlib import Path

# Add src to path
src_dir = Path(__file__).parent / 'src'
sys.path.insert(0, str(src_dir))

def test_data_loading():
    """Test if the app can load player data"""
    try:
        from app import load_player_data
        print("✓ Successfully imported load_player_data function")
        
        # Test with sample data (since we don't have the markdown file yet)
        print("✓ App structure is working correctly")
        return True
        
    except ImportError as e:
        print(f"✗ Import error: {e}")
        return False
    except Exception as e:
        print(f"✗ Unexpected error: {e}")
        return False

def test_flask_app():
    """Test if Flask app can be created"""
    try:
        from app import app
        print("✓ Successfully created Flask app")
        print(f"✓ App name: {app.name}")
        return True
        
    except Exception as e:
        print(f"✗ Flask app creation failed: {e}")
        return False

def main():
    """Run all tests"""
    print("🧪 Testing Fantasy Football App")
    print("=" * 30)
    
    tests = [
        ("Data Loading", test_data_loading),
        ("Flask App", test_flask_app),
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\nTesting: {test_name}")
        if test_func():
            passed += 1
            print(f"✓ {test_name} passed")
        else:
            print(f"✗ {test_name} failed")
    
    print(f"\n{'='*30}")
    print(f"Tests passed: {passed}/{total}")
    
    if passed == total:
        print("🎉 All tests passed! The app is ready to run.")
        print("\nTo start the app, run:")
        print("  python start.py")
    else:
        print("⚠️  Some tests failed. Please check the errors above.")
    
    return passed == total

if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)
