# ============================================
# PASSWORD CHECKER & HASHER
# Shows if your password is strong AND how websites secretly store it!
# ============================================

import hashlib  # Secret code maker
import re       # Pattern matching tool

def check_password_strength(password):
    """
    Grades your password like a teacher grades a test!
    Returns: (score 0-100, list of suggestions)
    """
    score = 0
    suggestions = []
    
    # Rule 1: Length check (longer = better)
    if len(password) >= 12:
        score += 25
    elif len(password) >= 8:
        score += 15
        suggestions.append("Make it 12+ characters for better security")
    else:
        suggestions.append("Too short! Use at least 8 characters")
    
    # Rule 2: Has uppercase letters? (A-Z)
    if re.search(r'[A-Z]', password):
        score += 20
    else:
        suggestions.append("Add uppercase letters (A-Z)")
    
    # Rule 3: Has lowercase letters? (a-z)
    if re.search(r'[a-z]', password):
        score += 20
    else:
        suggestions.append("Add lowercase letters (a-z)")
    
    # Rule 4: Has numbers? (0-9)
    if re.search(r'\d', password):
        score += 20
    else:
        suggestions.append("Add numbers (0-9)")
    
    # Rule 5: Has special characters? (!@#$%)
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 15
    else:
        suggestions.append("Add special characters (!@#$%)")
    
    return score, suggestions


def hash_password(password):
    """
    Turns password into a SHA-256 secret code.
    This is what REAL websites store instead of your actual password!
    """
    # SHA-256 is like a blender - you can't un-blend the smoothie!
    hash_object = hashlib.sha256(password.encode('utf-8'))
    secret_code = hash_object.hexdigest()  # Turn into readable letters/numbers
    
    return secret_code


def show_hash_demo(password):
    """
    Shows how changing ONE letter completely changes the secret code!
    """
    print("\n🔬 HASH DEMONSTRATION (How websites store passwords):")
    print("-" * 60)
    
    original_hash = hash_password(password)
    print(f"Your password:        '{password}'")
    print(f"Secret code (hash):   {original_hash[:20]}... (truncated)")
    
    # Show what happens if we change just one letter
    if len(password) > 1:
        modified = password[:-1] + ('A' if password[-1] != 'A' else 'B')
        modified_hash = hash_password(modified)
        print(f"\nIf we change to:     '{modified}'")
        print(f"New secret code:      {modified_hash[:20]}... (completely different!)")
        print("☝️  See? Even tiny changes make totally different codes!")


# ============================================
# MAIN PROGRAM STARTS HERE
# ============================================

if __name__ == "__main__":
    print("🔐 WELCOME TO PASSWORD SECURITY CENTER 🔐")
    print("This tool checks your password strength and shows how websites protect it!")
    
    # Get password from user (hidden input for privacy)
    import getpass
    password = getpass.getpass("\nEnter a password to test (hidden for safety): ")
    
    # Check strength
    score, tips = check_password_strength(password)
    
    # Show results with emojis
    print("\n" + "=" * 50)
    print("📊 STRENGTH REPORT")
    print("=" * 50)
    
    if score >= 90:
        grade = "🏆 EXCELLENT"
    elif score >= 70:
        grade = "✅ GOOD"
    elif score >= 50:
        grade = "⚠️  OKAY"
    else:
        grade = "❌ WEAK - Needs Improvement"
    
    print(f"Score: {score}/100")
    print(f"Grade: {grade}")
    
    # Show progress bar
    filled = int(score / 5)  # 20 characters = 100%
    bar = "█" * filled + "░" * (20 - filled)
    print(f"Bar:   [{bar}]")
    
    # Show tips if needed
    if tips:
        print("\n💡 Suggestions to improve:")
        for tip in tips:
            print(f"   • {tip}")
    else:
        print("\n🎉 Perfect password! No suggestions needed!")
    
    # Show the hash demo
    show_hash_demo(password)
    
    # Educational note
    print("\n" + "=" * 60)
    print("🎓 WHY THIS MATTERS:")
    print("   Real websites NEVER store your actual password!")
    print("   They store the 'hash' (secret code) instead.")
    print("   Even if hackers steal the database, they get gibberish!")
    print("=" * 60)
