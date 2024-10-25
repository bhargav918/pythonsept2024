def get_execution_result(cmd: str):
    p = subprocess.Popen(
        cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    output, err = p.communicate()

    output = output.decode("utf-8")
    err = err.decode("utf-8")

    print(f"\noutput:{output}")
    print(f"err   :{err}")


get_execution_result("ping google.com")
get_execution_result("ifconfig")
get_execution_result("ifconfigsda")