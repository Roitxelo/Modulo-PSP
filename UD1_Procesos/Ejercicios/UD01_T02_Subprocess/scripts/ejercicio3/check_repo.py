git_status = 
git_log = 
git_fetch = ['git', 'fetch']

estado_del_repo = "Repositorio limpio"
ultimo_commit = 
estado_fetch
cambios_en_remoto

dicc_claves_porcelain = 
    'M'
    'A'
    'R'
    'D'
    '??'

}

resultado_git_status = subprocess.run(git_status, capture_output=True, text=True, encoding="utf-8")

if resultado_git_status.returncode != 0:
    print("")
    sys.exit


if resultado_git_status.stdout != "":
    estado_del_repo = ""
    for l in resultado_git_status.stdout.splitlines():
        l = l.strip()
        if len(1) > 0:
            codigo = 