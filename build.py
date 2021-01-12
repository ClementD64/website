#!/usr/bin/env python3

import jinja2 as j2
import os

def get_active_page(filename):
  if filename == "index.html":
    return "/"
  return "/" + filename.replace(".html", "")

env = j2.Environment(
  loader=j2.FileSystemLoader('templates'),
  trim_blocks=True,
  lstrip_blocks=True
)

for file in os.scandir("templates"):
  if file.name.startswith("_"):
    continue
    
  page = env.get_template(file.name).render(
    active_page=get_active_page(file.name)
  )

  if not os.path.exists("dist"):
      os.makedirs("dist")

  with open(os.path.join("dist", file.name), "w") as f:
    f.write(page)