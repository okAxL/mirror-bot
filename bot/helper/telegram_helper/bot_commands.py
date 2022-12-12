from bot import CMD_INDEX
import os
def getCommand(name: str, command: str):
    try:
        if len(os.environ[name]) == 0:
            raise KeyError
        return os.environ[name]
    except KeyError:
        return command


class _BotCommands:
    def __init__(self):
        self.StartCommand = getCommand(f'START_CMD', f'start22{CMD_INDEX}')
        self.MirrorCommand = getCommand('MIRROR_CMD', f'mirror{CMD_INDEX}')
        self.UnzipMirrorCommand = getCommand('UNZIP_CMD', f'unzipmirror{CMD_INDEX}')
        self.ZipMirrorCommand = getCommand('ZIP_CMD', f'zipmirror{CMD_INDEX}')
        self.QbMirrorCommand = getCommand('QBMIRROR_CMD', f'qbmirror{CMD_INDEX}')
        self.QbUnzipMirrorCommand = getCommand('QBUNZIP_CMD', f'qbunzipmirror{CMD_INDEX}')
        self.QbZipMirrorCommand = getCommand('QBZIP_CMD', f'qbzipmirror{CMD_INDEX}')
        self.YtdlCommand =  getCommand('YTDL_CMD', f'ytdl22{CMD_INDEX}')
        self.YtdlZipCommand = getCommand('YTDLZIP_CMD', f'ytdlzip22{CMD_INDEX}')
        self.LeechCommand = getCommand('LEECH_CMD', f'leech22{CMD_INDEX}')
        self.UnzipLeechCommand = getCommand('UNZIPLEECH_CMD', f'unzipleech22{CMD_INDEX}')
        self.ZipLeechCommand = getCommand('ZIPLEECH_CMD', f'zipleech22{CMD_INDEX}')
        self.QbLeechCommand = getCommand('QBLEECH_CMD', f'qbleech22{CMD_INDEX}')
        self.QbUnzipLeechCommand = getCommand('QBZIPLEECH_CMD', f'qbunzipleech22{CMD_INDEX}')
        self.QbZipLeechCommand = getCommand('QBUNZIPLEECH_CMD', f'qbzipleech22{CMD_INDEX}')
        self.YtdlLeechCommand =getCommand('YTDLLEECH_CMD',  f'ytdlleech22{CMD_INDEX}')
        self.YtdlZipLeechCommand = getCommand('YTDLZIPLEECH_CMD', f'ytdlzipleech22{CMD_INDEX}')
        self.CloneCommand = getCommand('CLONE_CMD', f'cloneop{CMD_INDEX}')
        self.CountCommand = getCommand('COUNT_CMD', f'count22{CMD_INDEX}')
        self.DeleteCommand = getCommand('DELETE_CMD', f'del{CMD_INDEX}')
        self.CancelMirror = getCommand('CANCEL_CMD', f'cancel{CMD_INDEX}')
        self.CancelAllCommand = getCommand('CANCEL_ALL_CMD', f'cancelall{CMD_INDEX}')
        self.ListCommand = getCommand('LIST_CMD', f'listop{CMD_INDEX}')
        self.SearchCommand = getCommand('SEARCH_CMD', f'search22{CMD_INDEX}')
        self.StatusCommand = getCommand('STATUS_CMD', f'status{CMD_INDEX}')
        self.AuthorizedUsersCommand = f'users22{CMD_INDEX}'
        self.AuthorizeCommand = f'authorize22{CMD_INDEX}'
        self.UnAuthorizeCommand = f'unauthorize22{CMD_INDEX}'
        self.AddSudoCommand = f'addsudo22{CMD_INDEX}'
        self.RmSudoCommand = f'rmsudo22{CMD_INDEX}'
        self.PingCommand = f'ping{CMD_INDEX}'
        self.RestartCommand = f'restart{CMD_INDEX}'
        self.StatsCommand = f'stats{CMD_INDEX}'
        self.HelpCommand = f'help22{CMD_INDEX}'
        self.LogCommand = f'log22{CMD_INDEX}'
        self.ShellCommand = f'shell22{CMD_INDEX}'
        self.EvalCommand = f'eval22{CMD_INDEX}'
        self.ExecCommand = f'exec22{CMD_INDEX}'
        self.ClearLocalsCommand = f'clearlocals22{CMD_INDEX}'
        self.LeechSetCommand = f'leechset22{CMD_INDEX}'
        self.SetThumbCommand = f'setthumb22{CMD_INDEX}'
        self.BtSelectCommand = f'btsel22{CMD_INDEX}'
        self.SleepCommand = f'sleep22{CMD_INDEX}'
        self.RssListCommand = getCommand('RSSLIST_CMD', f'rsslist22{CMD_INDEX}')
        self.RssGetCommand = getCommand('RSSGET_CMD', f'rssget22{CMD_INDEX}')
        self.RssSubCommand = getCommand('RSSSUB_CMD', f'rsssub22{CMD_INDEX}')
        self.RssUnSubCommand = getCommand('RSSUNSUB_CMD', f'rssunsub22{CMD_INDEX}')
        self.RssSettingsCommand = getCommand('RSSSET_CMD', f'rssset22{CMD_INDEX}')
        self.AddleechlogCommand = getCommand('ADDLEECHLOG_CMD', f'addleechlog22{CMD_INDEX}')
        self.RmleechlogCommand = getCommand('RMLEECHLOG_CMD', f'rmleechlog22{CMD_INDEX}')
BotCommands = _BotCommands()
