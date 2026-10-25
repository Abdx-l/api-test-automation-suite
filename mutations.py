import os,subprocess,sys,json
results={}
baseline=subprocess.run([sys.executable,"-m","pytest","-q"],env={**os.environ,"MUTATION":""})
if baseline.returncode:raise SystemExit("baseline failed")
for mutation in ("status","auth","schema","paging","delete"):
 result=subprocess.run([sys.executable,"-m","pytest","-q"],env={**os.environ,"MUTATION":mutation})
 results[mutation]=result.returncode!=0
print(json.dumps(results,indent=2))
if not all(results.values()):raise SystemExit("surviving mutation")
