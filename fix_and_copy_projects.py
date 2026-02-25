import re

with open('index.html', 'r', encoding='utf-8') as f:
    idx_content = f.read()

# 1. Fix the closing tag of workflow in index.html
if '            </a>\n\n        </div>\n      </div>\n    </section>' not in idx_content:
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

# 2. Extract RetailGen and Workflow blocks directly
match = re.search(r'(<!-- Item 5: RetailGen.*?</a>\n\n            <!-- Item 6: Workflow.*?</a>)', idx_content, re.DOTALL)
if match:
    projects_html = match.group(1)
    
    # 3. Insert into work.html
    with open('work.html', 'r', encoding='utf-8') as f:
        work_content = f.read()

    # Find where to insert it: after linkedin block end, which ends with </a> close.
    # We will look for </a>\n\n                </div>\n            </section>
    
    if "RetailGen — Multimodal Semantic Engine" not in work_content:
        # replace the end of the grid
        work_content = work_content.replace(
"""                        </div>
                    </a>

                </div>
            </section>""",
f"""                        </div>
                    </a>

                    {projects_html}

                </div>
            </section>""")
            
        with open('work.html', 'w', encoding='utf-8') as f:
            f.write(work_content)

        print("Projects successfully copied to work.html")
    else:
        print("Projects already in work.html")
else:
    print("Failed to find projects in index.html")
