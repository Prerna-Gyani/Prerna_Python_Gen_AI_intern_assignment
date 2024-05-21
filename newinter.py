import tkinter as tk
import requests
import json

# Function to fetch data from the API and process citations
def fetch_and_process_data():
    url = "https://devapi.beyondchats.com/api/get_message_with_sources"
    response = requests.get(url)
    
    print("Response Content:", response.content)  # Debugging
    
    try:
        data = response.json()
    except json.JSONDecodeError:
        # If response is not JSON, display an error message
        output_text.config(state=tk.NORMAL)
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, "Error: Unable to fetch data from the API.")
        output_text.config(state=tk.DISABLED)
        return

    # Process data to identify citations
    citations = []
    for item in data:
        if isinstance(item, dict):
            response_text = item.get("message", "")  # Corrected key name
            sources = item.get("sources", [])
            if any(source in response_text for source in sources):
                citations.append(sources)
            else:
                citations.append([])
        else:
            # If item is not a dictionary, skip it
            continue

    # Display citations
    display_citations(citations)

# Function to display citations in the GUI
def display_citations(citations):
    citations_text = "\n".join([f"Citation {i+1}: ID - {c['id']}, Link - {c['link']}" for i, c in enumerate(citations)])
    output_text.config(state=tk.NORMAL)
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, citations_text)
    output_text.config(state=tk.DISABLED)

# Create GUI window
root = tk.Tk()
root.title("API Citation Checker")

# Add fetch button
fetch_button = tk.Button(root, text="Fetch Data", command=fetch_and_process_data)
fetch_button.pack(pady=10)

# Add text widget to display citations
output_text = tk.Text(root, height=15, width=50)
output_text.pack()

root.mainloop()
