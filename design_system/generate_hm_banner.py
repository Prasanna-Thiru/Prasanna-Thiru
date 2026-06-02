import os

# Create the output directory if it doesn't exist
os.makedirs('c:/Users/prasa/Desktop/NJ/Prasanna-Thiru/design_system', exist_ok=True)

width = 1200
height = 420

# Standard crisp SVG paths for minimalist white social icons (viewbox 0 0 24 24)
github_path = "M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.53 1.032 1.53 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z"
linkedin_path = "M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"
email_path = "M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"
globe_path = "M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 17.93c-3.95-.49-7-3.85-7-7.93 0-.62.08-1.21.21-1.79L9 15v1c0 1.1.9 2 2 2v1.93zm6.9-2.53c-.26-.81-1-1.4-1.9-1.4h-1v-3c0-.55-.45-1-1-1h-6v-2h2c.55 0 1-.45 1-1V7h2c1.1 0 2-.9 2-2v-.41c2.93 1.19 5 4.06 5 7.41 0 2.08-.8 3.97-2.1 5.4z"

svg = []
svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="{height}" style="background-color: #0d0d0d;">')
svg.append('  <defs>')
svg.append('    <style>')
svg.append('      @import url("https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600&amp;family=Satisfy&amp;display=swap");')
svg.append('      .social-icon { fill: #ffffff; opacity: 0.85; transition: opacity 0.2s; }')
svg.append('      .social-icon:hover { opacity: 1; }')
svg.append('      .concept-text { font-family: "Montserrat", sans-serif; font-size: 14px; font-weight: 300; fill: #d0d0d0; line-height: 1.8; letter-spacing: 0.5px; text-anchor: middle; }')
svg.append('      .signature-logo { font-family: "Satisfy", cursive; font-size: 58px; fill: #ffffff; text-anchor: middle; letter-spacing: 1px; }')
svg.append('      .location-text { font-family: "Montserrat", sans-serif; font-size: 11px; font-weight: 500; fill: #888888; letter-spacing: 3px; text-anchor: middle; text-transform: uppercase; }')
svg.append('    </style>')
svg.append('  </defs>')

# 1. Social Icons Deck at the top
svg.append('  <g transform="translate(600, 70)" text-anchor="middle">')
# GitHub Icon
svg.append(f'    <g transform="translate(-105, -12)" class="social-icon">')
svg.append(f'      <path d="{github_path}" transform="scale(1)" />')
svg.append('    </g>')
# LinkedIn Icon
svg.append(f'    <g transform="translate(-35, -12)" class="social-icon">')
svg.append(f'      <path d="{linkedin_path}" transform="scale(1)" />')
svg.append('    </g>')
# Email Icon
svg.append(f'    <g transform="translate(35, -12)" class="social-icon">')
svg.append(f'      <path d="{email_path}" transform="scale(1)" />')
svg.append('    </g>')
# Portfolio Icon
svg.append(f'    <g transform="translate(105, -12)" class="social-icon">')
svg.append(f'      <path d="{globe_path}" transform="scale(1)" />')
svg.append('    </g>')
svg.append('  </g>')

# 2. Centered custom H&M-like concept statement
svg.append('  <text class="concept-text">')
svg.append('    <tspan x="600" y="145">Prasanna Thiru\'s engineering concept is to offer high-quality Artificial Intelligence, Generative AI,</tspan>')
svg.append('    <tspan x="600" y="175">and RAG systems at the best performance in a scalable way. Prasanna has since his academic and professional</tspan>')
svg.append('    <tspan x="600" y="205">inception built state-of-the-art vector pipelines, robust full-stack apps, and predictive models. The content of</tspan>')
svg.append('    <tspan x="600" y="235">this profile is open-source and represents premium professional software craftsmanship.</tspan>')
svg.append('  </text>')

# 3. Prominent Luxury Brush Signature Logo
svg.append('  <text x="600" y="325" class="signature-logo">Prasanna Thiru</text>')

# 4. Location Link
svg.append('  <text x="600" y="380" class="location-text">Chennai, India | 🛰️</text>')

svg.append('</svg>')

output_path = 'c:/Users/prasa/Desktop/NJ/Prasanna-Thiru/banner.svg'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(svg))

print(f"H&M Style Minimalist Profile Banner SVG generated successfully at: {output_path}")
