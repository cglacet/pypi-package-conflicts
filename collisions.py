from itertools import product
import requests
import jellyfish
from bs4 import BeautifulSoup


def main():
    packages = packages_set()
    max_similarity_ratio = 1/3
    output_file_name = f'package_conflicts_{max_similarity_ratio:.3f}.csv'
    write_package_conflicts(packages, output_file_name, max_similarity_ratio=max_similarity_ratio)


def packages_set():
    r = requests.get('https://pypi.org/simple/')
    packages = set(BeautifulSoup(r.text, 'html.parser').get_text().split('\n'))
    packages.remove('')
    return packages


def write_package_conflicts(packages, file_name, **kwargs):
    with open(file_name, 'w+') as f:
        for (x, y) in package_conflicts(packages, **kwargs):
            f.write(f'{x}, {y}\n')


def package_conflicts(packages, max_similarity_ratio=1/3):
    for package_x, package_y in product(packages, repeat=2):
        if package_x <= package_y:
            continue
        distance = jellyfish.damerau_levenshtein_distance(package_x, package_y)
        min_len = min(len(package_x), len(package_y))
        if distance/min_len <= max_similarity_ratio:
            yield package_x, package_y


def test_package_set():
    return set(['ztfy.zmq', 'zthreadpool', 'ztilde', 'ztimer', 'ztlearn', 'ztm', 'ztools', 'ZtoRGBpy', 'ztpserver', 'ztq_console', 'ztq_core', 'ztq_worker', 'ztranslator', 'ztreamy', 'ztv', 'ztz', 'zuanfeng', 'zubbi', 'zubr', 'ZubyteSetuptool', 'zucchini', 'zuckup', 'zufaelliger', 'zugbruecke', 'zugexianshi', 'zugh', 'zuice', 'zuid', 'zula', 'zulip', 'zulip-beta', 'zulipbot', 'zulip-bots', 'zulip-botserver', 'zulip-term', 'zulu', 'zumanji', 'zumi', 'zumidashboard', 'zums', 'zumservices-api-py', 'zun', 'zunda-python', 'zun-tempest-plugin', 'zun-ui', 'zunzuncito', 'zuolar_nester', 'zuora', 'zuora-aqua-client-cli', 'zuora-client', 'zuorapy', 'zuoraquery', 'zuoyeji', 'zuper-auth', 'zuper-auth-z5', 'zuper-commons', 'zuper-commons-z5', 'zuper-ipce-comp', 'zuper-ipce-z5', 'zuper-nodes', 'zuper-nodes-python2', 'zuper-nodes-python2-daffy', 'zuper-nodes-python2-z5', 'zuper-nodes-z5', 'zuper-schemas', 'zuper-typing-z5', 'zuper-utils', 'zurb-foundation', 'zutil', 'zutils', 'zuul', 'zuul_get', 'zuul-registry', 'zuul-sphinx', 'zuup', 'zuzuvibhu', 'zvbot', 'zvdata', 'zvit', 'zVMCloudConnector', 'zvt', 'zw3ohpxuyg', 'zwatershed', 'zwave-mqtt-bridge', 'zwb-data', 'zwb-job', 'zwb-utils', 'zwc', 'zwdlib', 'zweb', 'Zwei', 'ZweiCogs', 'zweig', 'zwende', 'zw-flink', 'zwholder', 'zwift-client', 'Zwiki', 'zw.jsmath', 'zw.mail.incoming', 'zw_nester', 'zwoasi', 'zw-outliersdetec', 'zw.schema', 'zwsp-steg-py', 'zwt', 'zwt5', 'zwtestprint', 'zw.widget', 'zx', 'zx1995_nester', 'zxbasic', 'zx_core_backend', 'zxcvbn', 'zxcvbncpp', 'zxcvbn-dutch', 'zxcvbn-py3', 'zxcvbnpython', 'zxcvbn-python', 'zxd3', 'zxdnester', 'ZXD-nester', 'zxing', 'zxinglight', 'zxotest', 'zxpath', 'zxpath2', 'zxs', 'zxtestlib', 'zxtools', 'zxwei-nester', 'zy1221_nester', 'zy-aliyun-python-sdk', 'zybats', 'zyb-naster', 'zydis', 'zygomorphic', 'zygote', 'zyk_hfp_test1', 'zyklop', 'zyklus', 'zyl_nester', 'zylxd', 'zymbit', 'zymbit-connect', 'zymbit-trequests', 'zymkey', 'zymouse', 'zymp', 'zymptest', 'zymtest2', 'ZY_nester', 'zynet', 'zynlp', 'zype', 'zypper-patch-status-collector', 'ZypUtility', 'zy-tools', 'zyutil', 'zyw', 'zyzFlask', 'zyzz', 'zz', 'zzh', 'zzhfun', 'zzhmodule', 'ZZHnester', 'zzlog', 'zzltest', 'zzmm', 'zz_nester', 'zzr', 'zzyzx', 'zzz', 'zzzeeksphinx', 'zzzfs', 'zzzutils', 'zzz-web', 'zzzZZZzzz'])


if __name__ == "__main__":
    main()