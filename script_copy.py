import re

with open('index.html', 'r', encoding='utf-8') as f:
    idx_content = f.read()

# Fix closing tags first for item 6 if needed
if '            </a>\n\n        </div>\n      </div>\n    </section>' not in idx_content:
    print("Fixing closing tag in index.html")
    idx_content = idx_content.replace(
"""                  </svg>
                </div>
              </div>
          </div>

        </div>
      </div>
    </section>""",
"""                  </svg>
                </div>
              </div>
            </a>

        </div>
      </div>
    </section>""")
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(idx_content)

# Extract blocks using regex
match = re.search(r'(<!-- Item 5: RetailGen.*?</a>)\s*(?=</div>\s*</div>\s*</section>)', idx_content, re.DOTALL)
if match:
    projects_html = match.group(1)
    
    with open('work.html', 'r', encoding='utf-8') as f:
        work_content = f.read()
        
    if "RetailGen — Multimodal Semantic Engine" not in work_content:
        # We need to insert it right before the closing div of the grid in work.html
        # grid pattern is: </a> \n\n    </div> \n </section>
        replace_target = """                        </div>
                    </a>

                </div>
            </section>"""
            
        replacement = f"""                        </div>
                    </a>

{projects_html}

                </div>
            </section>"""
            
        if replace_target in work_content:
            work_content = work_content.replace(replace_target, replacement)
            with open('work.html', 'w', encoding='utf-8') as f:
                f.write(work_content)
            print("Successfully injected projects into work.html")
        else:
            print("Target string not found in work.html")
    else:
        print("Projects already inside work.html")
else:
    print("Failed to find projects with regex in index.html")
